```json
{
  "id": "de7543818f649f62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294662,
  "host_pid": "9e6742732c60:1",
  "hash": "6decefbeec480c2851ac9471ab9f673bf522c04c469cef1fea67c301971a6f9b",
  "cid": "QmV16decefbeec480c2851ac9471ab9f673bf522c04c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294662,
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
      "evaluated_at": 1760294662
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
  "sig": "971464fc7b3041b740000dc12d1456b50b9ac33f37e917e800fd43b0869e7485"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 87300048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}