```json
{
  "id": "abb4b8a99988f15f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290398,
  "host_pid": "9e6742732c60:1",
  "hash": "6cd0303335a512b71b920b57b4bb033d19adb80b81590145c8823e9bf92abf81",
  "cid": "QmV16cd0303335a512b71b920b57b4bb033d19adb80b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290398,
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
      "evaluated_at": 1760290398
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
  "sig": "b13fc6a7afbde6fb064808076dbcba31abaa34a93693402c590d1478edfef903"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028777791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'd241f2dd5b1f162a'}}}een': 1760285765, 'matching_hash': 'b26c49bc45dba458'}}}