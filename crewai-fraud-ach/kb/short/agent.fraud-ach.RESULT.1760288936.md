```json
{
  "id": "79be43366be763b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288936,
  "host_pid": "9e6742732c60:1",
  "hash": "0a6f7556c26c37ca3fd6b899af5cc497e414c4260b3f34946cb45656f1b0ead7",
  "cid": "QmV10a6f7556c26c37ca3fd6b899af5cc497e414c426",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288936,
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
      "evaluated_at": 1760288936
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
  "sig": "9b9ba91a3e09b2b48bd27689e5a14895898eefee5474a05f41503a49d319875f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 34370784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}