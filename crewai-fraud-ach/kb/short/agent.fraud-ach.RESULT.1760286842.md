```json
{
  "id": "5518d2e63d75229e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286842,
  "host_pid": "9e6742732c60:1",
  "hash": "23ba8f97519bf9251b106807812b98d557783ae04bc24068a1861090860f9ae2",
  "cid": "QmV123ba8f97519bf9251b106807812b98d557783ae0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286842,
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
      "evaluated_at": 1760286842
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
  "sig": "716fa597fe1d286a305cfa11d45d5b04dc2b3296cb2b809627d9b5dc6a32809f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464946217
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 39139445, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760284979, 'matching_hash': '76eefa6b67e55304'}}}