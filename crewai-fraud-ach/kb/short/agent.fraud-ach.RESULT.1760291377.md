```json
{
  "id": "518be5efb4181154",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291377,
  "host_pid": "9e6742732c60:1",
  "hash": "a5cc3f876d557efb482c1b321553710056b7bef161d22ca5a2d166785f98fcf2",
  "cid": "QmV1a5cc3f876d557efb482c1b321553710056b7bef1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291377,
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
      "evaluated_at": 1760291377
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "17a7c31a38210fa83ae5821030b190f4b772a685bb8ce2bbf36909eb0af4873e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 507153179781967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 36939306, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}