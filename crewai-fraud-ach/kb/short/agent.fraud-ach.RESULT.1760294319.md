```json
{
  "id": "2b10bc32bd6e5f56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294319,
  "host_pid": "9e6742732c60:1",
  "hash": "ac29db7f2ea6f996ee689a76222a0ca9eeaad2524ed3abbecdf92678a484acc5",
  "cid": "QmV1ac29db7f2ea6f996ee689a76222a0ca9eeaad252",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294319,
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
      "evaluated_at": 1760294319
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
  "sig": "9b64660f60a618626cb46a476f37244ad86d369c7d5ff290f5a9bcf832a28a54"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028645436
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 118000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '6242cc5f185f73d7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}