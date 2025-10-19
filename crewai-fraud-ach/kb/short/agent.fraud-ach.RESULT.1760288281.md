```json
{
  "id": "f79106210a98da52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288281,
  "host_pid": "9e6742732c60:1",
  "hash": "1c69a738277ac76681f764af4bcefddbed74096c88ed190068141df8e3a9461a",
  "cid": "QmV11c69a738277ac76681f764af4bcefddbed74096c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288281,
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
      "evaluated_at": 1760288281
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
  "sig": "186d2eadd1446fb5efc8bb35aaa0e7b152293091070b343c8e1fb392a26413b3"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201465841026
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 44000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285765, 'matching_hash': 'e2a83dab91a99cc0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}