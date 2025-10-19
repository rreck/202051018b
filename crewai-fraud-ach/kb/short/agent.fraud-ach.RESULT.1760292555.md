```json
{
  "id": "7b83e31791ee38cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292555,
  "host_pid": "9e6742732c60:1",
  "hash": "3bc72734b294acec06f857865b160f37a3abcfb9b73f01281494eadd2d18315e",
  "cid": "QmV13bc72734b294acec06f857865b160f37a3abcfb9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292555,
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
      "evaluated_at": 1760292555
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
  "sig": "a0e261867d0e89e97a397a9562ab8d4560413b18a67bef0a08c587de297e7328"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598774484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 39429400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': 'dadabb4a69349ebb'}}}