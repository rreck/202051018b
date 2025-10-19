```json
{
  "id": "a57c9beba941b299",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286028,
  "host_pid": "9e6742732c60:1",
  "hash": "920125b2dd6b8f2e50138f9613ec9564edd1cfe052994e3d71a0884bb3e16ac1",
  "cid": "QmV1920125b2dd6b8f2e50138f9613ec9564edd1cfe0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286028,
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
      "evaluated_at": 1760286028
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "992df9f6e519101b7e95ff4b73405d40d3457f9a8826d15b57738ea7df29d107"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 026009594828050
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}