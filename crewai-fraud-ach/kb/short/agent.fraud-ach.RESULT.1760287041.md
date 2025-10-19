```json
{
  "id": "7f46880849e2480e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287041,
  "host_pid": "9e6742732c60:1",
  "hash": "14a3fc85f3317da3d2c76aa1c9fa33840c364352f15355b9d6e2b0aab3d80e98",
  "cid": "QmV114a3fc85f3317da3d2c76aa1c9fa33840c364352",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287041,
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
      "evaluated_at": 1760287041
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
  "sig": "7e823adc6f13bf462983f2e1aead98733d011d54cc102637a85546c662efb2bd"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000020376030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17395084, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': '92ff62b724ca331a'}}}