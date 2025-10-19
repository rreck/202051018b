```json
{
  "id": "a9f92dbf76f509bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290351,
  "host_pid": "9e6742732c60:1",
  "hash": "dd19b41fbc5700de735c830c33d10e9295d80b6c09f085015e662420fa27565f",
  "cid": "QmV1dd19b41fbc5700de735c830c33d10e9295d80b6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290351,
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
      "evaluated_at": 1760290351
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
  "sig": "cee72373d776c670ee603c63d913dda4642f1636d3af5466f3d07f160bfad0db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240979962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 52631908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '0560549e1456bff1'}}}