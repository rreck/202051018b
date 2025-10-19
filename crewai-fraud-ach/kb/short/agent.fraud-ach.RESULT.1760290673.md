```json
{
  "id": "16a5f122d247348c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290673,
  "host_pid": "9e6742732c60:1",
  "hash": "3f3bd226214474ea923e04e962be627b73b093c1de6a0293209e97bfedf3dfa7",
  "cid": "QmV13f3bd226214474ea923e04e962be627b73b093c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290673,
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
      "evaluated_at": 1760290673
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
  "sig": "9788603aa58cd9f6a8b9577271cfbad8bc403d670f832b3ab09d9a20e222db3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036177444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 27607164, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285764, 'matching_hash': '11850a408d1201a4'}}}