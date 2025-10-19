```json
{
  "id": "143bd07d7b3ec083",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287302,
  "host_pid": "9e6742732c60:1",
  "hash": "3b1dfe680cddeac92e4558552558dc6c82f4b827e647ff3069df6d60a25abced",
  "cid": "QmV13b1dfe680cddeac92e4558552558dc6c82f4b827",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287302,
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
      "evaluated_at": 1760287302
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "552b9cd19198820e32432e63aaba999bdc5b23eb44b6423d93788e1558a17a2e"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 121000242075877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}