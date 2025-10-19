```json
{
  "id": "96daa0df7b17d421",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287965,
  "host_pid": "9e6742732c60:1",
  "hash": "0bbc312502a46e732623de4a451a3a575ede92e487ecb27c2bcb5419f80b3f89",
  "cid": "QmV10bbc312502a46e732623de4a451a3a575ede92e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287965,
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
      "evaluated_at": 1760287965
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
  "sig": "9a40056e9cc5b505fecfa592f19445700645ca232e6e1db9c4f87440556b4fd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020703113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 22428354, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': '6c2ac9b0cec56c2f'}}}