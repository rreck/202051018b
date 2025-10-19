```json
{
  "id": "15cbd57282b0ae75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285967,
  "host_pid": "9e6742732c60:1",
  "hash": "e80f8ad15dcada98a22077b554292610bbaf895c45c34a9dc428fa2881836460",
  "cid": "QmV1e80f8ad15dcada98a22077b554292610bbaf895c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285967,
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
      "evaluated_at": 1760285967
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
  "sig": "fe641c08793c8f5152ba751ad1460eff5a12619112fbf75cf87f5215fbeb6f78"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592077072
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}