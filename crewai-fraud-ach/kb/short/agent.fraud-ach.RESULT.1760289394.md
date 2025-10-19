```json
{
  "id": "249db16b31d1a95f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289394,
  "host_pid": "9e6742732c60:1",
  "hash": "f45ad514416d4e86a78805bb12c9caf949060d693443c79f24371824a6734a4b",
  "cid": "QmV1f45ad514416d4e86a78805bb12c9caf949060d69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289394,
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
      "evaluated_at": 1760289394
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
  "sig": "033bd847f75b964e9e346d76a19e19b5bd7b72e34d679a24632a2948af8a2dbb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463891034
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 25284378, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '2167bcd96d131e8f'}}}