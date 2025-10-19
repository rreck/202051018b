```json
{
  "id": "469335459e125b82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292750,
  "host_pid": "9e6742732c60:1",
  "hash": "e33bd22554cd921ea13c0fcae5ab28370f6c3f3890b7cc2a70c98d1de7ec313c",
  "cid": "QmV1e33bd22554cd921ea13c0fcae5ab28370f6c3f38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292750,
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
      "evaluated_at": 1760292750
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
  "sig": "f1c739fd61ae2ff400ae0e9af96ae17914266e9d3d0f3e4857b5927a68e746e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024587821
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 88049664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': 'e3fd1743fc412dec'}}}}