```json
{
  "id": "785825f725ca1698",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291142,
  "host_pid": "9e6742732c60:1",
  "hash": "d279d9738bf51525bf9586b996e254f4a074afdda468a959efb7621adb6804d4",
  "cid": "QmV1d279d9738bf51525bf9586b996e254f4a074afdd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291142,
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
      "evaluated_at": 1760291142
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
  "sig": "baafc108ad19eaf1622d83907dc6b8d38b9998c14ba6b7807f2989af2bc121d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 44783760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}