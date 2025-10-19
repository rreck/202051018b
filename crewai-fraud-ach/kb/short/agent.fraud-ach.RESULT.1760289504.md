```json
{
  "id": "f71aafa26eb572d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289504,
  "host_pid": "9e6742732c60:1",
  "hash": "2d5aacfeb6ba96127ce9bb07eafac1a20c4f5df81dee190f1e86dfd3ebe6724e",
  "cid": "QmV12d5aacfeb6ba96127ce9bb07eafac1a20c4f5df8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289504,
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
      "evaluated_at": 1760289504
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
  "sig": "dbb9c0958422e992bb8deba4e16e55ea44aa1911ca581a66d2d1da106a1c43aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}een': 1760285763, 'matching_hash': '227a4380e23ca7de'}}}