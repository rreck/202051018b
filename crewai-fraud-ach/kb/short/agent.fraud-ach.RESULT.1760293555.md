```json
{
  "id": "40d139a755b1e1c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293555,
  "host_pid": "9e6742732c60:1",
  "hash": "4ea01c29585d0afb202777bd00daf14ee3bfabced305ed6bd492c5bfe948899d",
  "cid": "QmV14ea01c29585d0afb202777bd00daf14ee3bfabce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293555,
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
      "evaluated_at": 1760293555
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
  "sig": "78512b56ad2823d897f973c6c60f8adea17787fe73e0ce1690205211892ad8f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027005922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 63335948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '8fe7ed8865cd9a2a'}}}}