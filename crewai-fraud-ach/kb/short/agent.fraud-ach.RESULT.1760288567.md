```json
{
  "id": "38aec041bf84654d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288567,
  "host_pid": "9e6742732c60:1",
  "hash": "e35cad45e11aff5e202f007b11e078ba3f7a0fce571f3ab6b3e344777b73e072",
  "cid": "QmV1e35cad45e11aff5e202f007b11e078ba3f7a0fce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288567,
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
      "evaluated_at": 1760288567
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
  "sig": "11435a6e5e0c335d71caf7bd11d72eedd7f4afd5949520f4bc140cb8d0e7a7b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}