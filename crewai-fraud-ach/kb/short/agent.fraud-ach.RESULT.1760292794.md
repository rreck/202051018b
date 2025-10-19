```json
{
  "id": "45e75e0510d6819e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292794,
  "host_pid": "9e6742732c60:1",
  "hash": "340c33804a3d35b8b3d55b3503bad882d206693d867b479ea51828d2cc2d673d",
  "cid": "QmV1340c33804a3d35b8b3d55b3503bad882d206693d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292794,
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
      "evaluated_at": 1760292794
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
  "sig": "db3ab9c76b36df0b215cbfb0ee0d713bf94e53777b63e35a91acb4249911c7ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465310802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 76673485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '86dc5261411570c1'}}}