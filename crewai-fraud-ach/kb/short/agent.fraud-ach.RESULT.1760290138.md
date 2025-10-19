```json
{
  "id": "c9fd8600f3609b37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290138,
  "host_pid": "9e6742732c60:1",
  "hash": "6109509a9f4703a6c8cf405d166a4f89b313e623cd40133fe1cdf7ae326f0729",
  "cid": "QmV16109509a9f4703a6c8cf405d166a4f89b313e623",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290138,
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
      "evaluated_at": 1760290138
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
  "sig": "c9ce50ddccb2e0aa9983c890aba9c9774e835540e24c02dc0814087e57daa306"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 26691598, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}