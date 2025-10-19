```json
{
  "id": "757effcbcf5bedfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293329,
  "host_pid": "9e6742732c60:1",
  "hash": "f034b8f009e9a08ac15aa983b190d3b6d692f9ba6e7434b85bbb40677d4197e0",
  "cid": "QmV1f034b8f009e9a08ac15aa983b190d3b6d692f9ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293329,
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
      "evaluated_at": 1760293329
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
  "sig": "1dc44fd1ad2ab4be4f967942875d3b9a2509242aa32bbb4ffa93964c2d6b7998"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154102308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 292, 'threshold': 50, 'total_amount': 107580684, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 291, 'first_seen': 1760284979, 'matching_hash': '687d8a253912c530'}}}aly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.46, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8549284}}}