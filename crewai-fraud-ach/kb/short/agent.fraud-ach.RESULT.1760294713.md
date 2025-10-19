```json
{
  "id": "1588e4f0d5cd93fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294713,
  "host_pid": "9e6742732c60:1",
  "hash": "d6d4a7ce411129440cf5f4885a9f6a6ec37b10e8ebbfa50f84b6550abd194f8b",
  "cid": "QmV1d6d4a7ce411129440cf5f4885a9f6a6ec37b10e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294713,
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
      "evaluated_at": 1760294713
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
  "sig": "a19d970734baa780c631e60ee4f094a442df6a40557476632e8fce44cf153617"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598774484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 47906721, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': 'dadabb4a69349ebb'}}}}