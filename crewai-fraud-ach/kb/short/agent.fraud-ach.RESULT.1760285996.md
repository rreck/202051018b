```json
{
  "id": "2f8721cbb4f5048f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285996,
  "host_pid": "9e6742732c60:1",
  "hash": "ae7118cbf5ed81455df563c1a9e6c956b3bd8f9893cb45c2dc5951189c1d4e36",
  "cid": "QmV1ae7118cbf5ed81455df563c1a9e6c956b3bd8f98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285996,
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
      "evaluated_at": 1760285996
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
  "sig": "7c776bf22593875beb3c5bfca13cf6141568a8cc486740712ab652fb0882dd46"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592077072
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}