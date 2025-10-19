```json
{
  "id": "5da533f26316ae61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293683,
  "host_pid": "9e6742732c60:1",
  "hash": "04d315c337c3a657da834df514c4792e45d593a89260211085c7e7c3892f5168",
  "cid": "QmV104d315c337c3a657da834df514c4792e45d593a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293683,
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
      "evaluated_at": 1760293683
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
  "sig": "5f64e18894798a463aed69f9e101aa3d8101394dec7780d8b60be5755991af72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242075877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 27920715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}