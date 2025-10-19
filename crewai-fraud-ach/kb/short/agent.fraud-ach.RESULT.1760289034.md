```json
{
  "id": "668ec680b3f99715",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289034,
  "host_pid": "9e6742732c60:1",
  "hash": "63b05043fd091581ebfe1afe6105f6adbbda6e5937f6254d567c42f5965da19c",
  "cid": "QmV163b05043fd091581ebfe1afe6105f6adbbda6e59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289034,
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
      "evaluated_at": 1760289034
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
  "sig": "8024c84ddff09f56d593339f44925d924dd4693edf6d3d9cf19ecc47087d7183"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 26692392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}