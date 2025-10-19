```json
{
  "id": "ed1c1998c1f576a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287793,
  "host_pid": "9e6742732c60:1",
  "hash": "96b162cb257ff562c133789f98fccdb1f4aa0e7a2ff229e2f3dafa1b104881c1",
  "cid": "QmV196b162cb257ff562c133789f98fccdb1f4aa0e7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287793,
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
      "evaluated_at": 1760287793
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
  "sig": "1d51c50a866a36d8b2fbf5237d89be724f4ae75adb206efb174c1afeb5a7fe94"
}
```

Fraud detected: invalid_routing (score: 91)
Transaction: 699349871536240
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 26908200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285765, 'matching_hash': '372ab63252fc0966'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '699349873', 'validation_error': 'Invalid routing number checksum'}}}