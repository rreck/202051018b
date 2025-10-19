```json
{
  "id": "f87053a9ca07c314",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290270,
  "host_pid": "9e6742732c60:1",
  "hash": "c98a365a8e9727e9206a31dd41169d3483b83b4b93804df9d7bf549cd3cda5f8",
  "cid": "QmV1c98a365a8e9727e9206a31dd41169d3483b83b4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290270,
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
      "evaluated_at": 1760290270
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
  "sig": "b39daefceac1f13a499d55c64f171bad75e0a311818b62c60e61e78dcdaf7ad2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591397699
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 21103132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': '338c84efe55c1d97'}}}