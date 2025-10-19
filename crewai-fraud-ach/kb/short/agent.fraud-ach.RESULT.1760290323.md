```json
{
  "id": "b762cac3d68c3bee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290323,
  "host_pid": "9e6742732c60:1",
  "hash": "abc278ae773963ea40a19bc30e2530077e42ec340e1f64e261c72e3634266e23",
  "cid": "QmV1abc278ae773963ea40a19bc30e2530077e42ec34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290323,
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
      "evaluated_at": 1760290323
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
  "sig": "7e9020279e4e76241673c5e513e6af543ead24a60f61b25753bfe38f37ff329d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274472610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 48351534, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285764, 'matching_hash': '7db40904e20d1f88'}}}