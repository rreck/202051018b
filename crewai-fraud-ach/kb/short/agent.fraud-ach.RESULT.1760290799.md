```json
{
  "id": "4f4e785e8028ed3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290799,
  "host_pid": "9e6742732c60:1",
  "hash": "72af7d988c799e66e4ca113a7f599243056c7b9195cbdc203481fbebfd34e45c",
  "cid": "QmV172af7d988c799e66e4ca113a7f599243056c7b91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290799,
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
      "evaluated_at": 1760290799
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
  "sig": "63886b6ab30547d68c2bc96cfd1853239d79e3dc0387c7d89369f8beab15a5b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 50601432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}