```json
{
  "id": "4a313f9231727abe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294724,
  "host_pid": "9e6742732c60:1",
  "hash": "096a632503f2ece3806c45457b57c83906519e14085a2d324924dc8262597e79",
  "cid": "QmV1096a632503f2ece3806c45457b57c83906519e14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294724,
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
      "evaluated_at": 1760294724
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
  "sig": "701a9493fb25005b46b5d409ebb9ae22b02cb1c4b69305ad17764f08f4924a5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467837924
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 24040233, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '256da828ea708baa'}}}