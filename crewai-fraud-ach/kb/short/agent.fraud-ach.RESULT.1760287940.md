```json
{
  "id": "444de4aa65cd27b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287940,
  "host_pid": "9e6742732c60:1",
  "hash": "4fd1af68dfc92091a4cd62c0cbef754023ea98bcd359f2ab80f3b2530374e4ba",
  "cid": "QmV14fd1af68dfc92091a4cd62c0cbef754023ea98bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287940,
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
      "evaluated_at": 1760287940
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
  "sig": "ad9f33614b26b0cf258fb73733dc6091bb87aa0e195a4b3a12994e1745fe7428"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026828395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': '40ce51f53058bb71'}}}