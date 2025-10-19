```json
{
  "id": "275a6fc516e392b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294386,
  "host_pid": "9e6742732c60:1",
  "hash": "ccd55edd6359ec50f6fa314b9d9ce3c66ef1e654599ddafb63906833fdb2d909",
  "cid": "QmV1ccd55edd6359ec50f6fa314b9d9ce3c66ef1e654",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294386,
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
      "evaluated_at": 1760294386
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
  "sig": "385818e2008ff9a613a7332033ea50ad9a722549911a5f54b1d3e8edc8a4b4ea"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000026930485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 118500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '3159baf1077152c6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}outing number checksum'}}}