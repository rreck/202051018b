```json
{
  "id": "facb68e3ffd06410",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290364,
  "host_pid": "9e6742732c60:1",
  "hash": "8eeb1c4800b1256774daaf2ed728b65ff457d56b38d781d616ae4a456a953373",
  "cid": "QmV18eeb1c4800b1256774daaf2ed728b65ff457d56b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290364,
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
      "evaluated_at": 1760290364
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
  "sig": "27453eab937ec6dff52732d6c05c95ba588e76b6376cb32bae47204c69a32f2b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033181833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 55358660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': '52cd22d87934f676'}}}