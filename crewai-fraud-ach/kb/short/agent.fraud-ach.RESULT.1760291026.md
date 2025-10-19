```json
{
  "id": "d9684553f0273da5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291026,
  "host_pid": "9e6742732c60:1",
  "hash": "237d25ad7aa9995b3a1986e35560adb91e7a97607dc12652c19a398cd3159541",
  "cid": "QmV1237d25ad7aa9995b3a1986e35560adb91e7a9760",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291026,
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
      "evaluated_at": 1760291026
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
  "sig": "80cff0e944474549849717b0247412e117a84041540c21fd5b116b2b231e485c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025341279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 67871925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'e2ff1695635a899d'}}}