```json
{
  "id": "9ac7f5b2b413ba91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290793,
  "host_pid": "9e6742732c60:1",
  "hash": "a81fcf61a66e490409437dc3b4589c06ae9d3f96a1433901424dcf1f7170ad06",
  "cid": "QmV1a81fcf61a66e490409437dc3b4589c06ae9d3f96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290793,
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
      "evaluated_at": 1760290793
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
  "sig": "1b751712cf36b927d5e932ba8be48fb4f585715e9791a8565e891461f9be9d33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 18027102, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}