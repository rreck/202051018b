```json
{
  "id": "d25efb6e60290ccd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287577,
  "host_pid": "9e6742732c60:1",
  "hash": "25d74f5b54bcc0a68c183933439c3fbddd586e9a12c9b45282b497a785e20487",
  "cid": "QmV125d74f5b54bcc0a68c183933439c3fbddd586e9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287577,
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
      "evaluated_at": 1760287577
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
  "sig": "fe25f01392779f868e51848afa646b77b1aff91b0afadc2848e4a31ebf18128c"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 026009596855798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 17168060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': 'aef06f437446325c'}}}