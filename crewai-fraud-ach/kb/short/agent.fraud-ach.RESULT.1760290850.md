```json
{
  "id": "ac41685213d72ed8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290850,
  "host_pid": "9e6742732c60:1",
  "hash": "d8014dcc054c2a8642ba5ab73bbe89e6e4ed722ca16ec07bf57959e7985f095f",
  "cid": "QmV1d8014dcc054c2a8642ba5ab73bbe89e6e4ed722c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290850,
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
      "evaluated_at": 1760290850
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
  "sig": "66d46acd42796dc6af5c2e9830e16f2b739492d5033b3548f74884aa36669a8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241272290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 27747384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': 'ac7868cb6249fe41'}}}