```json
{
  "id": "5efa7bfbb863e131",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286879,
  "host_pid": "9e6742732c60:1",
  "hash": "34788c0d59607ac78cdea475e747c5c34151ba70232adba3b688bff8df120e94",
  "cid": "QmV134788c0d59607ac78cdea475e747c5c34151ba70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286879,
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
      "evaluated_at": 1760286879
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
  "sig": "7854e98974248617bc8acb55c7a1e69141d18307bf375cdfb71cffc4f81e7f48"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17188480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}