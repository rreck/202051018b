```json
{
  "id": "18a11fa6b7f20fe2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289441,
  "host_pid": "9e6742732c60:1",
  "hash": "e5c718c062cfd5bc69e25c1efde4d93abc8979b04878616e358e66f4f6ef34ab",
  "cid": "QmV1e5c718c062cfd5bc69e25c1efde4d93abc8979b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289441,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289441
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "7ba8d914098fd5f508d14538ea6327c84f52855743af23839cabaa3e58159370"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 24793233, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}