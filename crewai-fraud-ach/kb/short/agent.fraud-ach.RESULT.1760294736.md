```json
{
  "id": "36ab4cdc02cc7d24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294736,
  "host_pid": "9e6742732c60:1",
  "hash": "dbc571820afd3dda7b84745ffeae146ab8f354d91c07052a63e1ab8b23043aaa",
  "cid": "QmV1dbc571820afd3dda7b84745ffeae146ab8f354d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294736,
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
      "evaluated_at": 1760294736
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
  "sig": "dd3dad6b43b89f17734fa3bf63c4d921579df665c05aa2314975eb24a70b8ac7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270650471
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 12338325, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}