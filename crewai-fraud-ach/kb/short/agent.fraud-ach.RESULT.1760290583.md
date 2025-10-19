```json
{
  "id": "6901afbb7bdeea98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290583,
  "host_pid": "9e6742732c60:1",
  "hash": "1a92b50a9685ecc985ebb98d8da260209bc59aae3aafb18c4d73ae88948173f4",
  "cid": "QmV11a92b50a9685ecc985ebb98d8da260209bc59aae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290583,
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
      "evaluated_at": 1760290583
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
  "sig": "0058b15369cc62986d594ff686aa66cc0f3f3a75c5a5741b6c12c17d21e9d448"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 14418404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}