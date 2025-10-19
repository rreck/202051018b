```json
{
  "id": "fed17b5ffeed90bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293171,
  "host_pid": "9e6742732c60:1",
  "hash": "b80ddf78bb0f1ec1052f6a101fab8bb33a727f2b51ad5e75421d6a60303d9542",
  "cid": "QmV1b80ddf78bb0f1ec1052f6a101fab8bb33a727f2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293171,
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
      "evaluated_at": 1760293171
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
  "sig": "2b7cee134ccef2a8aace1ecde6a0a0f0d47a6b82c5ac2e64e39214c3678cf06f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468298709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 13416657, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '7ee51499d35b3ada'}}}