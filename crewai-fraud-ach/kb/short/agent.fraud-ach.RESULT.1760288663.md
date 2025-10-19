```json
{
  "id": "3193691b0f77fa8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288663,
  "host_pid": "9e6742732c60:1",
  "hash": "82d7d1566473fe205a59fb4a5906d01768cdd604274430a09d9b0f1b9e6d9af0",
  "cid": "QmV182d7d1566473fe205a59fb4a5906d01768cdd604",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288663,
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
      "evaluated_at": 1760288663
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
  "sig": "c7a621fca08cea9343bae470ecba4b28effa440920c9d219915af70b5c7d60d4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 491975137325012
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 29469200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}