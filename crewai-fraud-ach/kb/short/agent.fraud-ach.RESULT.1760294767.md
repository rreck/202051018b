```json
{
  "id": "af72625cfa48bf53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294767,
  "host_pid": "9e6742732c60:1",
  "hash": "9444e0603e5352e2ae8c3fcd12c1a8c5c8636fe0f294756a784acdd052af3bbb",
  "cid": "QmV19444e0603e5352e2ae8c3fcd12c1a8c5c8636fe0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294767,
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
      "evaluated_at": 1760294767
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
  "sig": "3d6c061e44a7588a1991d40ad046e48674ab87d6e4443d061ae404c95f24389d"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463963144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 122000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': '4b7135c5b7384c49'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}