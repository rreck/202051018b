```json
{
  "id": "2d61424aaf70d703",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291659,
  "host_pid": "9e6742732c60:1",
  "hash": "825f6bbede1c5ba8b7319bd10667472b4dc412d93067674da0e4cef1871312c9",
  "cid": "QmV1825f6bbede1c5ba8b7319bd10667472b4dc412d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291659,
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
      "evaluated_at": 1760291659
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
  "sig": "873143fafcc8b832011d47fa041f368583440448636d0ced1eeeb382b7188dcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025069817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 85544820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '107b8433ca6199ca'}}}