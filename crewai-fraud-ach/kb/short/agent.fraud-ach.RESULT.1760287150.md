```json
{
  "id": "f2243de3920be682",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287150,
  "host_pid": "9e6742732c60:1",
  "hash": "547a26ba115bffa31e1fa4a5a37abf659ce284939f539e0442597e2a6387015d",
  "cid": "QmV1547a26ba115bffa31e1fa4a5a37abf659ce28493",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287150,
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
      "evaluated_at": 1760287150
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
  "sig": "cf890e765e9f3d66a00f05fd80f546855437968293821eb4bc792bdc16af21a5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000022956374
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': '4e30c52d3b71935d'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': '5f413645b746a025'}}}