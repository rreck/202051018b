```json
{
  "id": "c1f5cc291f85ce05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293342,
  "host_pid": "9e6742732c60:1",
  "hash": "0628cb7896d54646fe23cd82c845502462d15ab01e1fe523e515e84ee86f1c11",
  "cid": "QmV10628cb7896d54646fe23cd82c845502462d15ab0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293342,
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
      "evaluated_at": 1760293342
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
  "sig": "0419707a6203be86c7f535dd8c314de078982e96932546e3f216e8e755b9cd99"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 45339264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}