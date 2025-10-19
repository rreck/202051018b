```json
{
  "id": "93a639c70d2b9a3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289225,
  "host_pid": "9e6742732c60:1",
  "hash": "c98bb35ca026641762f05ae34aa940b2b8f0a636885406f7a307ed518b873991",
  "cid": "QmV1c98bb35ca026641762f05ae34aa940b2b8f0a636",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289225,
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
      "evaluated_at": 1760289225
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
  "sig": "e0f17b1699103e505abdfd455dbce31c2b66650cefd4f6214685c3584b4379a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 48582378, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}