```json
{
  "id": "c685a03782ea3be3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290137,
  "host_pid": "9e6742732c60:1",
  "hash": "13a933a9140d34e5b229a63257d8c1f1ee657fcb9d239b115879f083cbf1fdcb",
  "cid": "QmV113a933a9140d34e5b229a63257d8c1f1ee657fcb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290137,
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
      "evaluated_at": 1760290137
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
  "sig": "f768d3fac67bf8b90cab787bbd5575b36f7c863d5e575ae2703402149b19a437"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 61019104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}