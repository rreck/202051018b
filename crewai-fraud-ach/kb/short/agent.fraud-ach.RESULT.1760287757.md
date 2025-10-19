```json
{
  "id": "3d8f5bcec70676f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287757,
  "host_pid": "9e6742732c60:1",
  "hash": "30638304f3f54a16a098b5d291d8e6113103c3dc964cebe516a36aef59a85270",
  "cid": "QmV130638304f3f54a16a098b5d291d8e6113103c3dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287757,
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
      "evaluated_at": 1760287757
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
  "sig": "6bfa159896f1c468bd0d715b6454216e482e188354636518a0195b227334d8a2"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 34205883, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}