```json
{
  "id": "06562d9cf2157a42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287733,
  "host_pid": "9e6742732c60:1",
  "hash": "e72bc6af516ad8b66a923e8cfbcc87167f1ee7f559cb61a43cc6cb81de14166b",
  "cid": "QmV1e72bc6af516ad8b66a923e8cfbcc87167f1ee7f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287733,
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
      "evaluated_at": 1760287733
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
  "sig": "ccf6dc77d22a733011df611599c1591355d554522fce8f1f93cc12a6046c5b3c"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 29186990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}